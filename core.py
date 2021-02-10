import websites

def main(data,amazon,flipkart):
    #fe.show_page()
    a_title = ''
    a_price = ''
    a_url = ''
    f_title = ''
    f_price = ''
    f_url = ''
    if amazon:
        a_title, a_price, a_url = websites.amazon(data)
    if flipkart:
        f_title, f_price, f_url = websites.flipkart(data)
    return a_title, a_price, a_url, f_title, f_price, f_url
