class SmartHome:
    def __init__(self):
        self.lights_on = False
        self.fan_on = False
        self.security_armed = False
        self.log = []  # For storing actions

    def toggle_lights(self):
        self.lights_on = not self.lights_on
        action = "Lights turned ON" if self.lights_on else "Lights turned OFF"
        print(action)
        self.log.append(action)

    def toggle_fan(self):
        self.fan_on = not self.fan_on
        action = "Fan turned ON" if self.fan_on else "Fan turned OFF"
        print(action)
        self.log.append(action)

    def arm_security(self):
        self.security_armed = True
        action = "Security system ARMED"
        print(action)
        self.log.append(action)

    def disarm_security(self):
        self.security_armed = False
        action = "Security system DISARMED"
        print(action)
        self.log.append(action)

    def print_summary(self):
        print("\n--- Action Summary ---")
        for action in self.log:
            print("-", action)


# Example usage
home = SmartHome()

# Simulating commands
home.toggle_lights()
home.toggle_fan()
home.arm_security()
home.toggle_lights()
home.disarm_security()

# Print summary
home.print_summary()
