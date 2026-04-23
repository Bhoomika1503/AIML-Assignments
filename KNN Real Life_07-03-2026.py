# KNN Real Life Example

# Movie ratings
user_A = [5, 4, 3]
user_B = [4, 5, 3]
user_C = [1, 2, 5]

# Similarity check
score_AB = sum(user_A) - sum(user_B)
score_AC = sum(user_A) - sum(user_C)

print("User A vs User B similarity:", abs(score_AB))
print("User A vs User C similarity:", abs(score_AC))

if abs(score_AB) < abs(score_AC):
    print("User A is closer to User B")
    print("Recommend movies liked by User B")
else:
    print("User A is closer to User C")
    print("Recommend movies liked by User C")