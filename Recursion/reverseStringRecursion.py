def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
if __name__ == "__main__":
    result = reverse("aniruddha basak")
    print(result)
