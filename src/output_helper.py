def write_txt_file(data, output_path):
    # write txt file returns ok
    try:
        with open(output_path, 'w') as file:
            for line in data:
                file.write(f'{line}\r')
                print(f'line: {line}')
        return {'statusCode': 'ok', 'body': None}
    except Exception as e:
        return {'statusCode': 'error', 'body': e}


if __name__ == '__main__':
    filenames = ['data_page_09012022000000.json', 'data_page_09302022000000.json']
    data = [f'{f} - ok' for f in filenames]
    file_sufix = '09302022150001'
    output_path = f'../output_{file_sufix}.txt'
    result = write_txt_file(data, output_path)
    print(result)
