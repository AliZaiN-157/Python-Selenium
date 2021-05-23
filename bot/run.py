from booking.booking import Booking

# with Booking() as bot:
#     bot.land_first_page()
#     # bot.change_currency(currency='SAR')
#     bot.select_place_to_go("New York")
#     bot.select_date(check_in_date="2021-05-20",
#                     check_out_date="2021-05-29")
#     bot.select_adults(count=10)
#     bot.click_search()
#     bot.apply_filtrations()

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USA')
        bot.select_place_to_go('California')
        bot.select_date(check_in_date='2021-05-26',
                        check_out_date='2021-05-29')
        bot.select_adults(4)
        bot.click_search()
        bot.apply_filtrations()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
