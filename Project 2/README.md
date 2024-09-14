
# Fuzzy Logic Self-Driving Car Project

## Overview

This project is focused on designing a **fuzzy logic-controlled self-driving car** that can navigate a predetermined route without colliding with obstacles. The system uses ultrasonic sensors to evaluate distances from the car to surrounding obstacles, and it applies fuzzy logic to determine the steering angle and speed of the car.

The project is implemented in two phases:
1. **Phase 1**: Fuzzy logic is used to control the steering of the car based on the distance to obstacles.
2. **Phase 2**: In addition to steering, the speed of the car is also controlled by a fuzzy logic system.

## Project Goals

- **Steering Control**: The car's steering angle is adjusted based on the distance to the guardrails on both sides.
- **Speed Control**: In the second phase, the speed of the car is dynamically adjusted based on the distance to obstacles in front of the car.

## Implementation Phases

### Phase 1: Steering Control
- **Inputs**: 
  - Distance from the left front of the car to the guardrail.
  - Distance from the right front of the car to the guardrail.
- **Output**: 
  - Steering angle (rotation).
  
#### Steps:
1. **Fuzzification**: Convert the precise distance measurements into fuzzy values.
2. **Inference**: Apply fuzzy logic rules to determine the steering angle.
3. **Defuzzification**: Convert the fuzzy steering angle back into a precise value to control the car's steering.

### Phase 2: Speed Control
- **Input**: 
  - Distance from the front of the car to the obstacle.
- **Output**: 
  - Speed of the car.
  
#### Steps:
1. **Fuzzification**: Convert the distance measurements into fuzzy speed values.
2. **Inference**: Apply fuzzy logic rules to determine the car's speed.
3. **Defuzzification**: Convert the fuzzy speed value back into a precise speed for the car.

## Project Files

- **`fuzzy_controller.py`**: Controls the steering of the car based on fuzzy logic rules for distance to obstacles.
- **`additional_controller.py`**: Controls the speed of the car based on fuzzy logic rules for the distance to obstacles in front.
- **`rules.txt`**: Contains the fuzzy logic rules for steering.
- **`additional_rules.txt`**: Contains the fuzzy logic rules for speed control.

## Installation and Execution

To install the necessary libraries and run the project, follow these steps:

1. **Install Required Libraries**:
   ```bash
   pip install pygame
   ```

2. **Run the Simulator**:
   ```bash
   python simulator.py
   ```

During testing, you can control the car manually using the left and right arrow keys. Once the fuzzy logic system is implemented, the car will automatically adjust its steering and speed.

## Fuzzy Logic Methodology

- **Fuzzification**: The distance values are converted into fuzzy sets (e.g., close, moderate, far).
- **Inference**: Fuzzy rules are applied to determine the appropriate steering and speed.
- **Defuzzification**: The fuzzy outputs are converted back into precise steering angles and speed values.

## Notes

- Ensure that Phase 1 (steering control) is fully implemented before proceeding to Phase 2 (speed control).
- Use the provided resources and video tutorials to better understand the fuzzy logic system.

## Resources

- [Fuzzy Logic Video Tutorial 1](https://www.youtube.com/watch?v=TReelsVxWxg)
- [Fuzzy Logic Video Tutorial 2](https://www.youtube.com/watch?v=CBTEVFphv-E)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
