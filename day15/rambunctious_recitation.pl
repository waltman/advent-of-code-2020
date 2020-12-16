#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);

my %last_seen;
my $last;
my @init = split ',', $ARGV[0];
for my $t (0..$#init) {
    my $val = $init[$t];
    $last_seen{$val} = [$t+1];
    $last = $val;
}

for my $t (@init+1 .. 2020) {
    $last = do_turn(\%last_seen, $t, $last);
}

say "Part 1: ", $last;

for my $t (2021 .. 30_000_000) {
    $last = do_turn(\%last_seen, $t, $last);
}

say "Part 1: ", $last;

sub do_turn($last_seen, $t, $last) {
    my $prev = $last_seen->{$last};
    my $next_val;
    if (@$prev == 1) {
        $next_val = 0;
    } else {
        $next_val = $prev->[1] - $prev->[0];
    }

    if (defined $last_seen->{$next_val}) {
        my $old = $last_seen->{$next_val};
        my $i = (@$old == 2) ? 1 : 0;
        $last_seen->{$next_val} = [$old->[$i], $t];
    } else {
        $last_seen->{$next_val} = [$t];
    }

    return $next_val;
}
