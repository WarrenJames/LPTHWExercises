# Excercise 10: What was That?
# \n stands for new line character
# \ backslash character encodes difficult-to-type characters into a string.

# backslash out(escape) double-quote when using double-quotes
print "I am 6'2\" tall." # prints as I am 6'2" tall.
# backslash out(escape) single-quote when using single-quotes
print 'I am 6\'2" tall.' # prints as I am 6'2" tall.

# variable tabby_cat is equal to (escaped out tab) and "I'm tabbed in."
tabby_cat = "\tI'm tabbed in."
# variable persian_cat is equal to I'm a split(escaped out new line)on a line.
persian_cat = "I'm a split\non a line."
# variable backslash_cat is equal to I'm (escaped out "\") a (escaped out "\") cat.
backslash_cat = "I'm \\ a \\ cat."

# variable fat_cat is equal to long string (""") I'll do a list
# (escaped out tab)* Cat food
# (escaped out tab)* Fishies
# (escaped out tab)* Catnip(escaped out new line)(escaped out tab)* Grass
# end (""") string

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# prints as
##   I'm tabbed in.
print tabby_cat
# prints as
## I'm a split
## on a line.
print persian_cat
# prints as
## I'm \ a \ cat.
print backslash_cat
# prints as
## I'll do a list
##  * Cat food
##  * Fishies
##  * Catnip
##  * Grass
print fat_cat

print "\\" # Backslash
print "\'" # Single-quote (')
print "\"" # Double-quote (")
print "\a" # ASCII bell (BEL)
print "\b" # ASCII backspace (BS)
print "\f" # ASCII formfeed (FF)
print "\n" # ASCII linefeed (LF)
print "\N{name}" # Character named name in the Unicode database (Unicode only)
print "\r" # Carriage Return (CR)
print "\t" # Horizontal Tab (TAB)
print "\uxxxx" # Character with 16-bit hex value xxxx (u'' string only)
print "\Uxxxxxxxx" # Character with 32-bit hex value xxxxxxxx (u'' string only)
print "\v" # ASCII vertical tab (VT)
print "\ooo" # Character with octal value ooo
print "\ xhh" # Character with hex value hh (no space between \ and xhh)

# if string (i) is equal to /,-,|,\,or |
#   then print string(%s) \r(backspace) when string(%) is equal to the value of i, (/,-,|,\, or |)
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
# string prints as one of the characters in the string and presses backspace
#   then types the next character. 
