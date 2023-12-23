import openaq
import pandas as pd
import os


def request_data(filename, endpoint, **kwargs):
    '''
    Convenience function to avoid making too many API requests.

    Input:
        filename (str): name of file from which to read, or to which
            to write, the data
        endpoint (func): handle (name) of function used to make API
            request (e.g. api.measurements)
        **kwargs: keyword arguments to pass to endpoint
    
    Returns:
        df (pd.DataFrame): pandas dataframe containing requested data
    '''
    # Check if file already in current folder
    if filename not in os.listdir():
        # File not in folder: have to download data
        redownload = True
    else:
        # File already in folder; ask user if data needs updating
        user_confirm = input('Local file available. Request data again? [y/N] ')
        if user_confirm in ['y', 'Y', 'yes', 'aye']:
            redownload = True
        else:
            # Default behaviour is to use local file
            print('Reading from local file...')
            df = pd.read_csv(filename)
            redownload = False
    
    if redownload:
        # Make API request if user confirms
        print('Requesting data from API and writing to file...')
        df = endpoint(df=True, **kwargs)
        df.to_csv(filename)

    return df


if __name__ == '__main__':
    print('hello!')
    # api = openaq.OpenAQ()
    # df = request_data('data.csv', api.parameters)
    # print(df)