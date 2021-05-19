from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency='SAR')
    bot.select_place_to_go("New York")
    bot.select_date(check_in_date="2021-05-20",
                    check_out_date="2021-05-29")
    bot.select_adults(count=10)
    bot.click_search()
