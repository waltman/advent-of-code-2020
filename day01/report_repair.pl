#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);
use Algorithm::Combinatorics qw(combinations);
use List::Util qw(sum product);

my @entries = <>;
chomp @entries;

say 'Part 1: ', find_result(\@entries, 2);
say 'Part 2: ', find_result(\@entries, 3);

sub find_result($entries, $k) {
    my $iter = combinations($entries, $k);
    while (my $p = $iter->next) {
        return product($p->@*) if sum($p->@*) == 2020;
    }
}
