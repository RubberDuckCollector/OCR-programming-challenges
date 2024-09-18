def repeated_num_in_year(year: int) -> list[str]:
    year = str(year)

    repeated_chars = []

    for i in year:
        if year.count(i) > 1:
            if i in repeated_chars:
                pass
            else:
                repeated_chars.append(i)

    return repeated_chars


def main():
    print(repeated_num_in_year(2012))
    print(repeated_num_in_year(2013))


if __name__ == "__main__":
    main()
