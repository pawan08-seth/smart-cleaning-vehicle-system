from cleaning_system import CleaningSystem


def main():
    robot = CleaningSystem()

    while True:
        print("\n==== Smart Cleaning Vehicle ====")
        print("1. Start Cleaning")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            robot.start_cleaning()

        elif choice == "2":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()