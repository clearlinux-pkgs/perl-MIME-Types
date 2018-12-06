#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MIME-Types
Version  : 2.17
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MIME-Types-2.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MIME-Types-2.17.tar.gz
Summary  : 'Definition of MIME types'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
MIME::Types
===========
A start for a more detailed data-structure to keep knowledge
about various data types are defined by MIME.  Some basic
treatments with mime types are implemented.

%package dev
Summary: dev components for the perl-MIME-Types package.
Group: Development
Provides: perl-MIME-Types-devel = %{version}-%{release}

%description dev
dev components for the perl-MIME-Types package.


%prep
%setup -q -n MIME-Types-2.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/MIME/Type.pm
/usr/lib/perl5/vendor_perl/5.28.1/MIME/Type.pod
/usr/lib/perl5/vendor_perl/5.28.1/MIME/Types.pm
/usr/lib/perl5/vendor_perl/5.28.1/MIME/Types.pod
/usr/lib/perl5/vendor_perl/5.28.1/MIME/types.db
/usr/lib/perl5/vendor_perl/5.28.1/MojoX/MIME/Types.pm
/usr/lib/perl5/vendor_perl/5.28.1/MojoX/MIME/Types.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MIME::Type.3
/usr/share/man/man3/MIME::Types.3
/usr/share/man/man3/MojoX::MIME::Types.3
