#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);

my %questions;
my $num_groups = 0;
my $num_all = 0;
my $group_size = 0;

while (<>) {
    chomp;
    if ($_) {
        $group_size++;
        $questions{$_}++ for split //;
    } else {
        $num_groups += keys %questions;
        $num_all += grep {$_ == $group_size} values %questions;
        %questions = ();
        $group_size = 0;
    }
}

say "Part 1: ", $num_groups;
say "Part 2: ", $num_all;
