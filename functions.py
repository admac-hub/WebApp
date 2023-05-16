def get_todos(filepath='/home/devacuko/codeQueue/Python60Days/Day1/webapp/todo.txt'):
    
    '''
    Read the text file and return the list of to-do items 
    '''
    with open(filepath, 'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(todos_args, filepath='/home/devacuko/codeQueue/Python60Days/Day1/webapp/todo.txt'):
    '''
    Write the to-do list items in a text file
    '''
    with  open(filepath, 'w') as file:
            file.writelines(todos_args)

if __name__ == '__main__':
     print('Testing Fucntions')