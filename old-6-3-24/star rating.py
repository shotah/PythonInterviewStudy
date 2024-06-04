# Star Rating
# Have the function StarRating(str) take the str parameter being passed which will be an average rating between 0.00 and 5.00,
# and convert this rating into a list of 5 image names to be displayed in a user interface to represent the rating
# as a list of stars and half stars. Ratings should be rounded to the nearest half. There are 3 image file names
# available: "full.jpg", "half.jpg", "empty.jpg". The output will be the name of the 5 images
# (without the extension), from left to right, separated by spaces. For example: if str is "2.36"
# then this should be displayed by the following image:

# So your program should return the string "full full half empty empty".
# Examples
# Input: "0.38"
# Output: half empty empty empty empty
# Input: "4.5"
# Output: full full full full half


def StarRating(strParam):
    param = float(strParam)
    full_stars = int(param // 1)
    half_stars = 1 if param % 1 else 0
    empty_stars = 5 - full_stars - half_stars
    rating = (
        (full_stars * ["full"]) + (half_stars * ["half"]) + (empty_stars * ["empty"])
    )[:5]
    return " ".join(rating)


star = "0.38"
star = "3"
# star = "5"
# star = 1
s = StarRating(star)
print(s)
