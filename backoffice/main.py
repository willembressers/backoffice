from . import home_assistant, parse, pdf


def main():
    # get the data
    charger_data, tariff_data = home_assistant.data()

    # parse the data
    df = parse.both(charger_data, tariff_data)

    # generate the PDF
    pdf.generate(df)


if __name__ == "__main__":
    main()
