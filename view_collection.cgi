#!/usr/bin/perl -wT
require './logfile_helper.pl';
require './collection_helper.pl';

use strict;
use CGI;
use CGI::Carp qw ( fatalsToBrowser );
use File::Basename;
use File::Copy;


my $safe_characters = "a-zA-Z0-9_.-";

my $query = new CGI;
my $username = $query->param("username");
my $collection = $query->param("collection");

# Make sure username is ok:
if($username) {
    if ( $username =~ /^([$safe_characters]+)$/ ) {
	$username = $1;
    }
    else {
	die "Username contains invalid characters";
    }
    
    open(FP,"Logs/usernames.txt");
    my @all_users = readline(FP);
    close(FP);

    my $user_exist = 0;
    foreach my $i (@all_users) {
	$i =~ s/\n//;
	if($i eq $username) {
	    $user_exist = 1;
	}
    }
    if(!$user_exist) {
	die "User does not exist";
    }
}
else {
    die "Need to enter username";
}

# Make sure collection name is ok:
if($collection) {
    if ( $collection =~ /^([$safe_characters]+)$/ ) {
	$collection = $1;
    }
    else {
	die "Collection name contains invalid characters";
    }
}
else {
    die "Need to enter collection name";
}

# Write to logfile
#my $datestr2 = &GetTimeStamp;
#my $addr = $ENV{'REMOTE_ADDR'};
#open(FP,">>Logs/logfile.txt");
#print FP "\n$datestr2 $addr *upload_image Images/$upload_dir/$filename.jpg";
#close(FP);

# Send user to labeling tool page:
print $query->header ( );

&WriteViewCollectionPage($username,$collection);
