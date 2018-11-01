objects = $(wildcard *.in)
outputs := $(objects:.in=.txt)

all: $(outputs)

%.txt: %.in
	pip-compile -v --output-file $@ $<

# Local building of base requirements to Python2
base2.txt: base.in
	python2 -m piptools compile base.in -o base2.txt
