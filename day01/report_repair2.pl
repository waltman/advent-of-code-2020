#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);

my @entries;
while (<>) {
    chomp;
    push @entries, $_;
}

for my $i (0..$#entries-1) {
    for my $j ($i+1..$#entries) {
        if ($entries[$i] + $entries[$j] == 2020) {
            say 'Part 1: ', $entries[$i] * $entries[$j];
        }
    }
}

for my $i (0..$#entries-2) {
    for my $j ($i+1..$#entries-1) {
        for my $k ($j+1..$#entries) {
            if ($entries[$i] + $entries[$j] + $entries[$k] == 2020) {
                say 'Part 2: ', $entries[$i] * $entries[$j] * $entries[$k];
            }
        }
    }
}

