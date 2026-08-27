score = 174  # use this input when submitting your answer

# set award to its default value of None
award = None

# use the value of score to assign award to the correct prize name
if score <= 50:
    award = "wooden rabbit"
elif 151 <= score <= 180:
    award = "wafer-thin mint"
elif score >= 181:
    award = "penguin"

# use the truth value of award to assign message to the correct text
if award:
    message = "Congratulations! You won a {}!".format(award)
else:
    message = "Oh dear, no prize this time."

print(message)
