# Speaker script: how neural summaries are trained

Two slides, three clicks each. Roughly 30 to 40 seconds per slide. The bracketed
cues are the click that should already be on screen as you say the line.

## Slide 1: Regression (MSE)

**[Click 1: pipeline + loss equation]**
A weak-lensing map is huge, tens of thousands of pixels, so before any inference
we have to compress it. We train a neural network to turn the map into just a few
numbers, a summary t. The simplest way to do that is regression: we ask the
network to predict the cosmological parameters directly, and we penalize the
squared error to the truth.

**[Click 2: Gaussian posterior, "sufficient, lossless"]**
If you ask what minimizes that loss, the answer is the posterior mean. And that
is actually a strong summary: for a Gaussian posterior the mean is a sufficient
statistic, so you have thrown nothing away. The compression is lossless.

**[Click 3: two posteriors, same mean]**
The catch is that the mean is not sufficient in general. Here are two maps whose
posteriors share the same mean but have different shapes. Regression sends them to
the same summary, so it cannot tell them apart, and everything beyond the mean,
the non-Gaussian information, is lost.

## Slide 2: VMIM

**[Click 1: pipeline + objective]**
VMIM has the same goal, compress the map into a summary t, but it does not force t
to be the parameters. It lets t be any code, and it adds a second network, a
normalizing flow, whose job is to rebuild the full posterior from t. The two are
trained together to keep as much information about the parameters as possible.

**[Click 2: flow reshapes to match]**
As you maximize that information, the flow reshapes until it matches the true
posterior, non-Gaussian shape and all. At the optimum, t is a sufficient
statistic: the posterior given t is the same as the posterior given the whole map.

**[Click 3: payoff]**
So the contrast is simple. Regression keeps only the mean, the dot; VMIM keeps the
whole shape. For a Gaussian posterior the two agree, but our Universe is
non-Gaussian, and that is exactly where VMIM stays lossless and regression does
not.

---

### One-line version (if you are short on time)

"There are two ways to train the compressor: regression learns the posterior
mean, which is lossless only for Gaussian posteriors; VMIM maximizes mutual
information so the summary stays sufficient even when the field is non-Gaussian."
