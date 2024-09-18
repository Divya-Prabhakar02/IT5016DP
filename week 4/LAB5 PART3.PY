def categorize_request():
    total_amount = int(input("enter the total amount:$"))
    if total_amount< 150:
        print("LOW")
        print("Review for potential discount.")
    else:
        print("HIGH")
        print("Proceed with standard processing.")
def main():
    categorize_request()
main()





