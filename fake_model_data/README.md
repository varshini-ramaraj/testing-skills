Plan to have a SCG like model as an input, where you have multiple sets of data in the same concept 
- aka sites and customers, or production policies with different parts used for different things
Thus, the answer would be lugging a whole model around, vs lugging around just the parts needed.
- And writing tests vs none at all
- Maybe similarly about casing/so on.


- if it parses successfully, it passes
- else it fails
- so run everytime and get a fail- and thats painful

- Do not overcomplicate things! for me but also others lMAOOO
- Should I create a clean and a dirty version to make things easier on day of?
- start with dirty, write ideas of clean, only switch to clean on day of if needed may day may day
- Casing
- Expectations of data
- Parsing times maybe?
- Should logic be separated out , rather than having one function than has 100 lines of code
  - .....is it usually because youre reading a file, and assumptions from the top that lead to issues at the bottom
  - .....return type for something could be..a thing?
  - ICostProvider sorta situation - switchh/if else situation
  - something along -> fields that 
  - # # Shwoing some NO code might not be a bad idea - to show an example of how it might work
  - # # Maybe lets brainstorm it as a process, in order to see how that goes!
  - # # Explain data model issues, and mocking the entire thing, and how changing one thing can be a domino effect
  - initializer needs like 10-15 items, and will throw errors otherwise
  - initializer starts running functions breaking it down, and so mocking doesnt really work either
- Need items in the fake model data that need to be used together, and things that need to be used separately
  - such that we can have a - why would you do all of it together, just do some of it?
- Should there be tests at all? I guess to the point of clean version then yes but ..?

- make it a version of code we normally look at, dont make it too complex too
- look up opened file on pycharm
- Reading files
- Calculating something
- Parameter leading to an if else

- 1st use case is easy code the one I'm writing, 2nd use case is lets go look at NO 