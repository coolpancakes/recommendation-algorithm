# Recommendation engine based on user input, 14/07/2024 | coolpancakes on github.com

def information(desired_size):
    small_dog_breeds = [
        "Affenpinscher",
        "American Eskimo Dog",
        "American Hairless Terrier",
        "Basenji",
        "Beagle"
    ]

    medium_dog_breeds = [
        "Australian Cattle Dog",
        "Australian Shepherd",
        "Basset Hound",
        "Staffordshire Bull Terrier",
        "Soft Coated Wheaten Terrier"
    ]

    large_dog_breeds = [
        "Akita",
        "Alaskan Malamute",
        "American Bulldog",
        "American Staffordshire Terrier",
        "Anatolian Shepherd Dog"
    ]

    if desired_size == "small":
        print("\nHere are some suggestions for "
              "{} breeds:\n".format(desired_size))
        small_count = 0
        for small_breeds in small_dog_breeds:
            print("{}".format(small_breeds))

    elif desired_size == "medium":
        print("\nHere are some suggestions for "
              "{} breeds:\n".format(desired_size))
        medium_count = 0
        for medium_breeds in medium_dog_breeds:

            print("{}".format(medium_breeds))

    elif desired_size == "large":
        print("\nHere are some suggestions for "
              "{} breeds:\n".format(desired_size))
        large_count = 0
        for large_breeds in large_dog_breeds:
            print("{}".format(large_breeds))


def main():
    # Search input to search for information.
    desired_dog_size = input("What size dog are you after (small/medium/large)? ")
    information(desired_dog_size)


if __name__ == "__main__":
    main()
