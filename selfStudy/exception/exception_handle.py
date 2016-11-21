try:
    something = input("Enter text:")
except EOFError:
    print("Why did you do and EOF on me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
else: ## same c#, java finally statement
    print("You entered.. {}".format(something))

