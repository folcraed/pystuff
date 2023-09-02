"""
The cover price for a book is $24.95, but the bookstore gets a 40% discount.
Shipping costs $3 for the first copy, and 75 censts for each additional copy.
What would be the total cost for 60 copies?
"""

# Breaking it out into chunks, one could do something like this
discount = 24.95 * .40
bookstore_cost = 24.95 - discount
first_book = bookstore_cost + 3
other_books = 59 * .75
other_books_cost = (bookstore_cost * 59) + other_books
total = first_book + other_books_cost
print(total)

"""
An easier way would be to multiply the total number of books being bought by
the actual percentage bookstore cost (60% of cover price) with the per-book shipping
added. Then add the $3 single book cost minus one .75 cost.
"""

# This way reduces the calculation to a single line
print( 60 * (0.6 * 24.95 + 0.75) + (3 - 0.75) )
