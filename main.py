import sys
from anki_connect import add_note

def run_cli():
  print(f"{'--- ANKI CLI ADDER ---':.^30}")
  print("Write 'exit' to close the program.\n")

  while True:
    front = input(f"{'Word (English)':.<20}: ").strip() #strip = trim

    if front.lower() == "exit":
      print("Chao!")
      break

    if not front:
      print("Please, enter a word.")
      continue

    translation = input(f"{'Translation (spanish)':.<20}: ").strip()
    use_case = input(f"{'Enter an example sentence using the word:\n'}").strip()

    back = f"{translation}<br><br><b>Example:</b><br><i>{use_case}</i>"

    success, message = add_note(front, back)

    if success:
      print(f"{message}\n")
    else:
      print(f"{message}\n")
    
if __name__ == "__main__":
  try:
    run_cli()
  except KeyboardInterrupt:
    print("\n Program interruped. Leaving...")
    sys.exit(0)