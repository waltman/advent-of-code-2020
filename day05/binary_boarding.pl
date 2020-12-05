#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);

sub decode_row($row) {
    $row =~ tr/FB/01/;
    return eval("0b$row");
}

sub decode_col($col) {
    $col =~ tr/LR/01/;
    return eval("0b$col");
}

sub calc_seat_id($row, $col) {
    return $row * 8 + $col;
}

my $best_id = -1;
my $min_row = 1e300;
my $max_row = -1;
my %seats;
while (<>) {
    chomp;
    my $row = decode_row(substr($_, 0, 7));
    my $col = decode_col(substr($_, 7));
    my $seat_id = calc_seat_id($row, $col);
    $best_id = $seat_id if $seat_id > $best_id;
    $min_row = $row if $row < $min_row;
    $max_row = $row if $row > $max_row;
    $seats{"$row,$col"} = 1;
}

say "Part 1: $best_id";

for my $row ($min_row+1..$max_row-1) {
    for my $col (0..7) {
        unless (defined $seats{"$row,$col"}) {
            say "Part 2: ", calc_seat_id($row, $col);
        }
    }
}
