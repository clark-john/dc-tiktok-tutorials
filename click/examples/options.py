from click import (
  command, 
  option, 
  secho, 
  Choice,
  IntRange
)

# single value
@command()
@option('--color', '-c', default='cyan')
def run(color):
  secho("Hello", fg=color)

# multiple values in one option

@command()
@option('--fbg', help='Foreground and background text', nargs=2)
def run(fbg):
  fg, bg = fbg
  secho("Hello", fg=fg, bg=bg)

# multiple options

@command()
@option('--txt', help='first and second', multiple=True)
def run(txt):
  for x in txt:
    print(x)

# option repetition

@command()
@option('-v','--verbose', count=True)
def run(verbose):
  for x in range(verbose):
    print(x)

# Boolean options

@command()
@option('--settings', is_flag=True)
def run(settings):
  if settings:
    print("Settings")

# Feature switches

@command()
@option(
  '--square', 
  'exponent',
  default=True,
  flag_value='square'
)
@option(
  '--cube',
  'exponent',
  flag_value='cube'
)
def run(exponent):
  if exponent == 'square':
    print("Ten squared")
  else:
    print("Ten cubed")

# choice options

@command()
@option(
  '--language',
  type=Choice(['Java', 'Python', 'Ruby'],
  case_sensitive=False
  )
)
def run(language):
  if language == 'Java':
    print(
"""
class JavaHelloWorld {
  public static void main(String[] args){
    System.out.println("Hello World");
  }
}"""
    )
  elif language == 'Python':
    print("print(\"Hello World\")")
  else:
    print("puts Hello World")

# prompting

@command()
@option('--numbers', '-n', prompt=True)
def run(numbers):
  numbers = int(numbers)
  e = []
  for x in range(numbers):
    e.append(x)
  print(e)

# password

@command()
@option(
  'password',
  '-p', 
  hide_input=True, 
  prompt=True, 
  # confirmation_prompt=True,
  help='Type your password'
)
def run(password):
  if password == 'admin':
    secho("You can now enter admin mode",bold=True,fg='bright_green')
  else:
    secho("Wrong password", bold=True, fg='red')

# dynamic defaults for prompts
from platform import system

@command()
@option(
  '--system',
  prompt=True,
  default=lambda: system()
)
def run(system):
  secho("You're using "+system+' as of now.', fg='bright_yellow')

# callback and eager options

# example 1 (easy version)
from platform import python_version

def python_ver(ctx, param, value):
  if not value:
    ctx.abort()
  secho(python_version(), fg='green')
  ctx.exit()

@command()
@option(
  '--python-ver',
  is_flag=True,
  callback=python_ver
)
def run():
  pass

# yes params

def if_false(ctx, param, value):
  if not value:
    ctx.abort()
    # this says "Aborted!"
@command()
@option(
  '-y',
  is_flag=True,
  expose_value=False,
  prompt='Are you sure you want to reset quiz configuration?',
  callback=if_false
)
def run():
  secho("Settings successfully has been reset.", fg='bright_green')

# other prefix

# example 1
@command()
@option(
  '/italic;/no-italic'
)
def run(italic):
  secho("Hi guys", italic=italic)

# example 2
@command()
@option(
  ':pos',
  nargs=2,
)
def run(pos):
  x, y = pos
  print('X position:',x)
  print('Y position:',y)

# range options:

@command()
@option(
  '--number',
  type=IntRange(1, 30),
  help='Choose numbers from 1 to 30'
)
def run(number):
  print(number)

# optional value

@command()
@option(
  '--quiz',
  is_flag=False,
  flag_value='Declared Quiz',
  default='Quiz'
)
def run(quiz):
  print(quiz)

if __name__ == '__main__':
  run()