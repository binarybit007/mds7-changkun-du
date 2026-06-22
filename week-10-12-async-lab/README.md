
# Green AI Trade-Off Experiment

## Dataset
Fashion-MNIST dataset.

## Model
Deep Multi Layer Perceptron.

Architecture:

- Flatten layer
- Dense 512
- Dense 256
- Dense 128
- Dense 64
- Dense 32
- Output layer


## Experiments

A:
50% data, 50 epochs

B:
50% data, 100 epochs

C:
100% data, 50 epochs

D:
100% data, 100 epochs


## Conclusion

The goal was to compare model accuracy against carbon emissions.

Increasing the dataset size improved accuracy, but the increase was not
proportional to the additional computational cost.

Increasing epochs from 50 to 100 improved accuracy slightly but increased
energy consumption.

The best production model should balance accuracy and emissions.

The winning configuration is the model which achieves strong accuracy
with lower CO2 emission instead of simply using maximum data and epochs.
