# FANTASY STAR ONLINE

### see it's a pun

I decided to use data and automation to literally kek a fantasy football league and maybe decimate Fanduel.

### what works what don't
- [ ] play by play data
	- [x] for certain game
      - [ ] human legible 
- [ ] player data
	- [ ] from certain years
    - [ ] from certain games
	- [ ] calc best player for position
- [ ] team data
- [ ] make full fantasy team
	- [ ] with choice of position
  - [ ] WITH BUDGET (because fanduel)

### how to develop the garbage if you want for some godforsaken reason

there's not really any specific instructions BUT you have to do

`import nfl_data_py as nfl`

`years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
	            2016, 2017, 2018, 2019, 2020]`

`nfl.cache_pbp(years, downcast=False, alt_path=None)`

do this in IDLE and in order. then let it bake until golden brown. this will cache a lot of data for you and make the total time you waste on my garbage easier