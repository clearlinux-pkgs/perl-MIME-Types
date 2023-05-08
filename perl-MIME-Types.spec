#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MIME-Types
Version  : 2.24
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MIME-Types-2.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MIME-Types-2.24.tar.gz
Summary  : 'Definition of MIME types'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-MIME-Types-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
=   Generated on Wed Dec  9 10:29:07 2020 by OODoc 2.02
There are various ways to install this module:

%package dev
Summary: dev components for the perl-MIME-Types package.
Group: Development
Provides: perl-MIME-Types-devel = %{version}-%{release}
Requires: perl-MIME-Types = %{version}-%{release}

%description dev
dev components for the perl-MIME-Types package.


%package perl
Summary: perl components for the perl-MIME-Types package.
Group: Default
Requires: perl-MIME-Types = %{version}-%{release}

%description perl
perl components for the perl-MIME-Types package.


%prep
%setup -q -n MIME-Types-2.24
cd %{_builddir}/MIME-Types-2.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MIME::Type.3
/usr/share/man/man3/MIME::Types.3
/usr/share/man/man3/MojoX::MIME::Types.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
