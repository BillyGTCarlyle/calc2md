.POSIX:

PREFIX = /home/$(USER)/.config/libreoffice/4/user/

install:
	mkdir -p $(DESTDIR)$(PREFIX)/Scripts/python
	mkdir -p $(DESTDIR)$(PREFIX)/dialogs/calc2md
	cp -f scripts/markdown.py $(DESTDIR)$(PREFIX)/Scripts/python
	cp -f dialogues/markdown.xdl $(DESTDIR)$(PREFIX)/dialogs/calc2md/

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/Scripts/python/markdown.py
	rm -f $(DESTDIR)$(PREFIX)/dialogs/calc2md/markdown.xdl

.PHONY: install uninstall
