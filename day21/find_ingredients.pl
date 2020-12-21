#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);

my %h;
while (<>) {
    m/contains (.*)\)/;
    my @ingredients = split ', ', $1;
    for my $i (@ingredients) {
        $h{$i} = 1;
    }
}

for my $i (sort keys %h) {
    say $i;
}
