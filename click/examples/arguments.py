from click import ( 
  command, 
  argument, 
  secho, 
  option, 
)

# basic arguments

@command()
@argument('language')
def run(language):
  language = language.capitalize()
  if language == 'Python':
    print("print(\'Hello World\')")
  elif language == 'C++':
    print(
"""
#include <iostream>
using namespace std;
int main(){
  cout << "Hello World";
  return 0;
}""")
  elif language == 'Ruby':
    print("puts Hello World")
  elif language == 'Haskell':
    print(
"""
main :: IO ()
main = putStrLn "Hello World" """)
  elif language == 'Go':
    print(
"""
package main
import "fmt"
func main(){
  fmt.Println("Hello World")
}""")
  else:
    pass

# variadic args

@command()
@argument('languages', nargs=-1)
@argument('list', nargs=1)
def run(languages, list):
  for x in languages:
    secho(x+' added to '+list, fg='bright_green')

if __name__ == '__main__':
  run()

