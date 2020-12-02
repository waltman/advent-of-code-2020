#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);

sub letter_count($letter, @password_letters) {
    return scalar grep {/$letter/} @password_letters;
}

sub is_valid($letter, $p1, $p2, @password_letters) {
    return ($password_letters[$p1-1] eq $letter) ^ $password_letters[$p2-1] eq $letter;
}

my $count1 = 0;
my $count2 = 0;

while (<>) {
    chomp;
    my ($times, $letter, $password) = split;
    my ($start, $end) = split '-', $times;
    $letter =~ s/://;
    my @password_letters = split //, $password;
    $count1++ if $start <= letter_count($letter, @password_letters) <= $end;
    $count2++ if is_valid($letter, $start, $end, @password_letters);
}

say "Part 1: $count1";
say "Part 2: $count2";
