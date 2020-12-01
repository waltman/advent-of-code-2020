#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);
use Algorithm::Combinatorics qw(combinations);
use List::Util qw(sum product);

my @entries;
while (<>) {
    chomp;
    push @entries, $_;
}

my $iter = combinations(\@entries, 2);
while (my $p = $iter->next) {
    if (sum(@$p) == 2020) {
        say 'Part 1: ', product(@$p);
        last;
    }
}

$iter = combinations(\@entries, 3);
while (my $p = $iter->next) {
    if (sum(@$p) == 2020) {
        say 'Part 2: ', product(@$p);
        last;
    }
}
