# Movie Ratings Control Task
film_rating = "film_rating"

while True:
    film_rating = str(input("What is your film rating (or type 'exit' to leave):  ").upper())
    if film_rating == "UNIVERSAL" or film_rating == "U":
        print("everyone can watch")

    elif film_rating == "PG":
        print("General viewing, but some scenes may be unsuitable for young children")

    elif film_rating == "12A" or film_rating == "12":
        print("Films classified 12A and video works classified 12 contain material that"
              "\nis not generally suitable for children aged under 12."
              "\nNo one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

    elif film_rating == "15":
        print("No one younger than 15 may see a 15 film in a cinema")

    elif film_rating == "18":
        print("No one younger than 18 may see a 18 film in a cinema")

    elif film_rating == "EXIT":
        print("Thank you for using this program")
        break

    else:
        print("The film rating entered is invalid, please enter a valid "
              "film rating \nor type 'exit' to leave the program")
