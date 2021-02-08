#import fetch_data
import data_handler as dh
import front_end as fe
def main(data):
    #fe.show_page()
    a_title, a_price, a_url, f_title, f_price, f_url = dh.main(data)
    return a_title, a_price, a_url, f_title, f_price, f_url
