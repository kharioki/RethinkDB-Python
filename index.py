from rethinkdb import r

# connect to the database
r.connect('localhost', 28015).repl()

# create table
r.db('mydb').table_create('users').run()
