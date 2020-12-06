#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.32);
use experimental qw(signatures);
use Set::Scalar;

sub valid_hgt($v) {
    my $val = substr($v, 0, -2);
    my $unit = substr($v, -2);
    if ($unit eq 'cm') {
        return 150 <= $val <= 193;
    } elsif ($unit eq 'in') {
        return 59 <= $val <= 76;
    } else {
        return 0;
    }
}

my $keys = Set::Scalar->new(qw(byr iyr eyr hgt hcl ecl pid cid));
my $ecl = Set::Scalar->new(qw(amb blu brn gry grn hzl oth));

my %valid_field = (
                   byr => sub($v) { 1920 <= $v <= 2002 },
                   iyr => sub($v) { 2010 <= $v <= 2020 },
                   eyr => sub($v) { 2020 <= $v <= 2030 },
                   hgt => sub($v) { valid_hgt($v) },
                   hcl => sub($v) { $v =~ /^#[0-9a-f]{6}$/ },
                   ecl => sub($v) { $ecl->has($v) },
                   pid => sub($v) { $v =~ /^\d{9}$/ },
                   cid => sub($v) { 1 },
                  );

my $num_valid = 0;
my $num_valid2 = 0;
my $missing = $keys->clone;
my $ok = 1;
while (<>) {
    chomp;
    if ($_) {
        while (/(.{3}):([^ ]+)/g) {
            my $k = $1;
            my $v = $2;
            $missing->delete($k);
            $ok = 0 unless $valid_field{$k}($v);
        }
    } else {
        if ($missing->is_empty || ($missing->size == 1 && $missing->has('cid'))) {
            $num_valid++;
            $num_valid2++ if $ok;
        }
        $missing = $keys->clone;
        $ok = 1;
    }
}

say "Part 1: $num_valid";
say "Part 2: $num_valid2";

