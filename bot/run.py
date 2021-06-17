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
        bot.change_currency(currency='USD')
        bot.select_place_to_go(input("Where you want to go ?"))
        bot.select_date(input("What is the check in date ?"),
                        input("What is the check out date ?"))
        bot.select_adults(int(input('How many people ?')))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()
        bot.report_results()


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
