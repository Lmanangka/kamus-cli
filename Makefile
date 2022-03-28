PREFIX := ~/
all: install
install:
	cp kamus.py $(DESTDIR)$(PREFIX)bin/kamus
	chmod 0755 $(DESTDIR)$(PREFIX)bin/kamus
uninstall:
	$(RM) $(DESTDIR)$(PREFIX)bin/kamus
.PHONY: all install uninstall
