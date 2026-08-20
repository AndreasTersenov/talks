/* ===========================================================================
 * SBI pipeline explainer — "from kappa-maps to the posterior"
 * ---------------------------------------------------------------------------
 * One reveal.js slide that assembles the wavelet-summary neural-posterior-
 * estimation pipeline across five acts:
 *   1  cosmoGRID kappa-maps        (image asset: cosmogrid_box.png)
 *   2  + noise / wavelet transform -> wavelet-scale maps + summary stats
 *                                  (image asset: wavelet_scales_stats.png)
 *   3  the summaries condition a neural density estimator (conditional MAF)
 *   4  the flow pushes a Gaussian N(0,1) base into the posterior p(theta|x)
 *   5  trained by maximizing log-prob: L = -log p_phi(theta|x)   (JAX)
 *
 * The two map figures are real PNGs (positioned HTML <img>, faded per act). The
 * canvas draws the rest: the + noise arrow, the condition rail, the conditional
 * MAF network, the Gaussian base, and the sample points flowing into the
 * posterior contours. Text/maths are HTML+KaTeX labels. Self-contained; own
 * SBIPipeline namespace and .sbi-* selectors. Act 1 = default; four .sbi-frag
 * markers step to acts 2..5.
 * ======================================================================== */
(function (global) {
  "use strict";

  var C_INK = "#1b2733", C_MUTE = "#8b95a0", C_ACC = "#0072B2", C_WARM = "#d96a1f";

  /* ------------------------------- helpers ------------------------------- */
  function mulberry32(s){return function(){s|=0;s=(s+0x6D2B79F5)|0;var t=Math.imul(s^(s>>>15),1|s);
    t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
  function gaussian(rng){var u=1-rng(),v=rng();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
  function lerp(a,b,t){return a+(b-a)*t;}
  function ease(t){return t<0.5?2*t*t:1-Math.pow(-2*t+2,2)/2;}
  function clamp01(v){return v<0?0:(v>1?1:v);}
  function hexA(h,a){var r=parseInt(h.substr(1,2),16),g=parseInt(h.substr(3,2),16),b=parseInt(h.substr(5,2),16);
    return"rgba("+r+","+g+","+b+","+a+")";}
  function fitCanvas(c){var dpr=Math.min(window.devicePixelRatio||1,2),r=c.getBoundingClientRect();
    var w=r.width||(c.width/2),h=r.height||(c.height/2);c._w=w;c._h=h;c._dpr=dpr;
    c.width=Math.round(w*dpr);c.height=Math.round(h*dpr);}
  function tweenStep(cur,tgt,keys,sm){var moving=false;for(var i=0;i<keys.length;i++){var k=keys[i],d=tgt[k]-cur[k];
    if(Math.abs(d)>1e-4){cur[k]+=d*sm;moving=true;}else cur[k]=tgt[k];}return moving;}
  function arrowHead(ctx,x,y,ang,col,s){s=s||9;ctx.save();ctx.fillStyle=col;ctx.translate(x,y);ctx.rotate(ang);
    ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(-s,-s*0.55);ctx.lineTo(-s,s*0.55);ctx.closePath();ctx.fill();ctx.restore();}

  /* ---- warped-Gaussian contours (base = round, posterior = banana) ------- */
  function ptOf(P,u,v){var a=u,b=v-P.bend*(u*u-1);var ax=a*P.sx,by=b*P.sy,cr=Math.cos(P.rot||0),sr=Math.sin(P.rot||0);
    return[P.cx+ax*cr-by*sr,P.cy+ax*sr+by*cr];}
  function contourPath(ctx,P,r){ctx.beginPath();for(var i=0;i<=64;i++){var ph=i/64*2*Math.PI;
    var p=ptOf(P,r*Math.cos(ph),r*Math.sin(ph));if(i===0)ctx.moveTo(p[0],p[1]);else ctx.lineTo(p[0],p[1]);}ctx.closePath();}
  function drawContours(ctx,P,col,alpha){if(alpha<=0.01)return;ctx.save();ctx.globalAlpha=alpha;
    var lev=[2.05,1.15];for(var i=0;i<lev.length;i++){contourPath(ctx,P,lev[i]);
      ctx.fillStyle=hexA(col,i===0?0.13:0.22);ctx.fill();ctx.lineWidth=2;ctx.strokeStyle=hexA(col,0.85);ctx.stroke();}ctx.restore();}

  /* ============================== engine ================================= */
  function Engine(root){
    this.root=root;
    this.canvas=root.querySelector(".sbi-canvas");
    this.captionEl=root.querySelector(".sbi-caption");
    this.labels=root.querySelectorAll(".sbi-lbl, .sbi-img");
    this.nActs=5; this.act=1; this.running=false; this.autoTimer=null;
    var rng=mulberry32(2024); this.pts=[];
    for(var i=0;i<120;i++) this.pts.push({bx:gaussian(rng),by:gaussian(rng),u:gaussian(rng),v:gaussian(rng),ph:rng()});
    this.cur=this._stateForAct(1); this.tgt=this._stateForAct(1);
    fitCanvas(this.canvas); this._applyCopy(1); this._updateLabels(1);
    var self=this; this._loop=function(){self._frame();};
    window.addEventListener("resize",function(){fitCanvas(self.canvas);self._draw();});
  }
  Engine.prototype.resize=function(){fitCanvas(this.canvas);this._draw();};
  Engine.prototype._stateForAct=function(a){return{ fwd:a>=2?1:0, cond:a>=3?1:0, flow:a>=4?1:0 };};
  Engine.prototype.goTo=function(a){a=Math.max(1,Math.min(this.nActs,a));this.act=a;
    this.tgt=this._stateForAct(a);this._applyCopy(a);this._updateLabels(a);this.start();};
  Engine.prototype.snapTo=function(a){this.cur=this._stateForAct(a);this.goTo(a);};
  Engine.prototype.start=function(){if(!this.running){this.running=true;requestAnimationFrame(this._loop);}};
  Engine.prototype.autoplay=function(){var s=this;if(this.autoTimer)clearInterval(this.autoTimer);
    this.snapTo(1);var a=1;this.autoTimer=setInterval(function(){a+=1;
      if(a>s.nActs){clearInterval(s.autoTimer);s.autoTimer=null;return;}s.goTo(a);},2600);};
  Engine.prototype._frame=function(){
    var moving=tweenStep(this.cur,this.tgt,["fwd","cond","flow"],0.10);
    this._draw(); if(moving)requestAnimationFrame(this._loop); else this.running=false;};

  Engine.prototype._updateLabels=function(act){
    for(var i=0;i<this.labels.length;i++){var l=this.labels[i];
      l.classList.toggle("on", act>=(+l.getAttribute("data-appear")||1));}};
  Engine.prototype._applyCopy=function(act){var c=Engine.COPY[act];if(!c)return;
    this.captionEl.innerHTML='<span class="sbi-actno">'+act+'/'+this.nActs+'</span>'+c;
    if(global.renderMathInElement) try{global.renderMathInElement(this.captionEl,
      {delimiters:[{left:"\\(",right:"\\)",display:false}],throwOnError:false});}catch(e){}};

  Engine.COPY={
    1:"We take <b>cosmoGRID V1</b> forward simulations: spherical convergence maps \\(\\kappa\\) at known cosmologies \\(\\theta\\).",
    2:"Add <span class='c-warm'>shape noise</span> and a <span class='c-warm'>wavelet transform</span>, then measure <b>summary statistics</b> on each scale: the data vector \\(x\\).",
    3:"Those summaries <b>condition</b> a neural density estimator, a <span class='c-acc'>conditional MAF</span>.",
    4:"The flow turns a simple Gaussian \\(\\mathcal{N}(0,1)\\) into the <span class='c-acc'>posterior</span> \\(p(\\theta\\mid x)\\).",
    5:"Trained by maximizing the log-probability of the true parameters: \\(\\mathcal{L}=-\\log p_\\phi(\\theta\\mid x)\\)."
  };

  /* ------------------------------ drawing -------------------------------- */
  Engine.prototype._draw=function(){
    var cv=this.canvas, ctx=cv.getContext("2d"), W=cv._w, H=cv._h, st=this.cur;
    ctx.setTransform(cv._dpr,0,0,cv._dpr,0,0); ctx.clearRect(0,0,W,H);

    // geometry (fractions of the stage); images are positioned in the HTML
    var boxRight=0.183*W, wavLeft=0.232*W, wavRight=0.688*W, rowY=0.655*H;
    var baseC=[0.15*W,0.285*H], netC=[0.40*W,0.285*H], postC=[0.62*W,0.27*H];

    /* ---- + noise / wavelet-transform arrow (between the two figures) ---- */
    if(st.fwd>0.01){ctx.save();ctx.globalAlpha=st.fwd;
      ctx.strokeStyle=C_WARM;ctx.lineWidth=2.6;
      ctx.beginPath();ctx.moveTo(boxRight+6,rowY);ctx.lineTo(wavLeft-12,rowY);ctx.stroke();
      arrowHead(ctx,wavLeft-12,rowY,0,C_WARM,9);ctx.restore();}

    /* ---- condition rail: from the summary stats up into the network ---- */
    if(st.cond>0.01){ctx.save();ctx.globalAlpha=st.cond;
      var railX=wavRight+6, upY=0.455*H, netBot=netC[1]+0.092*H;
      ctx.strokeStyle=hexA(C_MUTE,0.95);ctx.lineWidth=2;
      ctx.beginPath();
      ctx.moveTo(railX,rowY-0.02*H); ctx.lineTo(railX,upY); ctx.lineTo(netC[0],upY); ctx.lineTo(netC[0],netBot);
      ctx.stroke();
      arrowHead(ctx,netC[0],netBot,-Math.PI/2,C_MUTE,8);ctx.restore();
      this._drawNet(ctx,netC,W,H,st.cond);
      drawContours(ctx,{cx:baseC[0],cy:baseC[1],sx:0.04*W,sy:0.04*W,bend:0,rot:0},C_MUTE,st.cond*0.9);
    }

    /* ---- the flow: sample points base -> posterior contours ---- */
    var P={cx:postC[0],cy:postC[1],sx:0.05*W,sy:0.058*H,bend:0.52,rot:0};
    if(st.flow>0.01){
      drawContours(ctx,P,C_ACC,st.flow);
      var p=ease(st.flow);
      ctx.save();
      for(var i=0;i<this.pts.length;i++){var pt=this.pts[i];
        var pp=clamp01((p-0.12*pt.ph)/0.88);
        var b=[baseC[0]+pt.bx*0.038*W, baseC[1]+pt.by*0.038*W];
        var t=ptOf(P,pt.u,pt.v);
        var x=lerp(b[0],t[0],pp), y=lerp(b[1],t[1],pp);
        ctx.fillStyle=hexA(C_ACC,0.55);ctx.beginPath();ctx.arc(x,y,2.2,0,2*Math.PI);ctx.fill();}
      ctx.restore();
    }
  };

  Engine.prototype._drawNet=function(ctx,c,W,H,alpha){
    ctx.save();ctx.globalAlpha=alpha;
    var layers=[5,5,3], xs=[c[0]-0.05*W,c[0],c[0]+0.05*W], colH=0.155*H, pos=[];
    for(var L=0;L<layers.length;L++){pos.push([]);
      for(var n=0;n<layers[L];n++){var y=c[1]-colH/2 + colH*(n/(layers[L]-1||1));pos[L].push([xs[L],y]);}}
    ctx.strokeStyle=hexA(C_INK,0.16);ctx.lineWidth=1;
    for(var l=0;l<layers.length-1;l++)for(var a=0;a<pos[l].length;a++)for(var b=0;b<pos[l+1].length;b++){
      ctx.beginPath();ctx.moveTo(pos[l][a][0],pos[l][a][1]);ctx.lineTo(pos[l+1][b][0],pos[l+1][b][1]);ctx.stroke();}
    for(var L2=0;L2<pos.length;L2++)for(var m=0;m<pos[L2].length;m++){
      ctx.fillStyle="#fff";ctx.strokeStyle=hexA(C_INK,0.6);ctx.lineWidth=1.4;
      ctx.beginPath();ctx.arc(pos[L2][m][0],pos[L2][m][1],6,0,2*Math.PI);ctx.fill();ctx.stroke();}
    ctx.restore();};

  /* ====================== reveal.js integration =========================== */
  var SBIPipeline={
    _engines:[],
    attach:function(Reveal){var self=this;
      var init=function(){var nodes=document.querySelectorAll("[data-sbi-explainer]");
        for(var i=0;i<nodes.length;i++){if(nodes[i]._sbiEngine)continue;
          var eng=new Engine(nodes[i]);nodes[i]._sbiEngine=eng;
          if(global.renderMathInElement) try{global.renderMathInElement(nodes[i],
            {delimiters:[{left:"\\(",right:"\\)",display:false},{left:"\\[",right:"\\]",display:true}],throwOnError:false});}catch(e){}
          self._engines.push({section:nodes[i],engine:eng});self._wireReplay(nodes[i],eng);}
        self._sync(Reveal);};
      if(Reveal&&Reveal.isReady&&Reveal.isReady())init();
      else if(Reveal)Reveal.on("ready",init);
      else document.addEventListener("DOMContentLoaded",init);
      if(Reveal){Reveal.on("fragmentshown",function(){self._sync(Reveal);});
        Reveal.on("fragmenthidden",function(){self._sync(Reveal);});
        Reveal.on("slidechanged",function(){self._engines.forEach(function(e){if(e.engine.resize)e.engine.resize();});self._sync(Reveal);});}
      document.addEventListener("keydown",function(ev){if(ev.key==="r"||ev.key==="R"){
        var on=self._cur(Reveal);if(on)on.autoplay();}});},
    _wireReplay:function(s,eng){var b=s.querySelector(".sbi-replay");
      if(b)b.addEventListener("click",function(e){e.preventDefault();e.stopPropagation();eng.autoplay();});},
    _cur:function(Reveal){if(!Reveal)return this._engines[0]&&this._engines[0].engine;
      var c=Reveal.getCurrentSlide();for(var i=0;i<this._engines.length;i++)if(this._engines[i].section===c)return this._engines[i].engine;return null;},
    _sync:function(Reveal){this._engines.forEach(function(e){
      var frags=e.section.querySelectorAll(".sbi-frag"),shown=0;
      for(var i=0;i<frags.length;i++)if(frags[i].classList.contains("visible"))shown+=1;
      e.engine.goTo(1+shown);});}
  };
  global.SBIPipeline=SBIPipeline;
})(window);
