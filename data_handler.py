import websites

def main(data):
    ####

    # Write code to get value from the form regarding which website to work with and the product

    ####
    product = data
    a_title, a_price, a_url = websites.amazon(product)
    f_title, f_price, f_url = websites.flipkart(product)
    return a_title, a_price, a_url, f_title, f_price, f_url
