import random
import os
import sys

class WomenSafetyChatbot:
    def __init__(self):
        # Create resources directory
        try:
            os.makedirs('resources', exist_ok=True)
        except Exception as e:
            print(f"Error creating resources directory: {e}")
            sys.exit(1)

        # Safety Resources
        self.safety_resources = {
            "emergency_contacts": [
                {"name": "Police Helpline", "number": "100"},
                {"name": "Women Helpline", "number": "1091"},
                {"name": "Safe Transport", "number": "1092"}
            ],
            "safety_tips": [
                "Always share your live location with trusted contacts.",
                "Keep emergency numbers saved in your phone.",
                "Trust your instincts if you feel unsafe.",
                "Learn basic self-defense techniques.",
                "Stay aware of your surroundings."
            ]
        }

    def get_emergency_help(self):
        """Generate emergency contact information"""
        print("\n🚨 EMERGENCY CONTACTS 🚨")
        for contact in self.safety_resources['emergency_contacts']:
            print(f"• {contact['name']}: {contact['number']}")
        return "Emergency contacts displayed."

    def provide_safety_tips(self):
        """Generate safety tips"""
        print("\n🛡️ SAFETY TIPS 🛡️")
        tips = random.sample(self.safety_resources['safety_tips'], 3)
        for tip in tips:
            print(f"• {tip}")
        return "Safety tips displayed."

    def emergency_protocol(self):
        """Show emergency protocol"""
        print("\n🚨 EMERGENCY PROTOCOL 🚨")
        protocol = [
            "Stay Calm and Assess Situation",
            "Call Emergency Helpline (100)",
            "Send SOS to Trusted Contacts",
            "Move to a Safe, Public Area",
            "Document Any Evidence",
            "Seek Immediate Help"
        ]
        for step in protocol:
            print(f"• {step}")
        return "Emergency protocol displayed."

    def interactive_chat(self):
        """Main chatbot interaction interface"""
        print("\n🛡️ WOMEN SAFETY SUPPORT CHATBOT 🛡️")
        print("Available Commands:")
        print("1. 'help' - Show Emergency Contacts")
        print("2. 'tips' - Get Safety Tips")
        print("3. 'protocol' - Emergency Protocol")
        print("4. 'exit' - End Conversation")

        while True:
            try:
                # Ensure input works in different environments
                user_input = input("\nEnter your command: ").lower().strip()
                
                # Exit condition
                if user_input in ['exit', 'quit', 'bye']:
                    print("Stay Safe! Goodbye.")
                    break
                
                # Command handling
                if user_input == 'help':
                    self.get_emergency_help()
                elif user_input == 'tips':
                    self.provide_safety_tips()
                elif user_input == 'protocol':
                    self.emergency_protocol()
                else:
                    print("Invalid command. Try 'help', 'tips', 'protocol', or 'exit'.")
            
            except KeyboardInterrupt:
                print("\nChat interrupted. Exiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    try:
        chatbot = WomenSafetyChatbot()
        chatbot.interactive_chat()
    except Exception as e:
        print(f"Failed to start chatbot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()