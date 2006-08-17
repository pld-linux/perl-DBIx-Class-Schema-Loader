#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Class-Schema-Loader
Summary:	DBIx::Class::Schema::Loader - Dynamic definition of a DBIx::Class::Schema
#Summary(pl):	
Name:		perl-DBIx-Class-Schema-Loader
Version:	0.03007
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BL/BLBLACK/DBIx-Class-Schema-Loader-0.03007.tar.gz
# Source0-md5:	1ade07990e2f9f364e586ac351108cfd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor >= 0.22
BuildRequires:	perl-Class-Data-Accessor >= 0.02
BuildRequires:	perl-Data-Dump >= 1.06
BuildRequires:	perl-DBD-SQLite >= 1.12
BuildRequires:	perl-DBIx-Class >= 0.06003
BuildRequires:	perl-Lingua-EN-Inflect >= 1.89
BuildRequires:	perl-Lingua-EN-Inflect-Number >= 1.1
BuildRequires:	perl-UNIVERSAL-require >= 0.1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Class::Schema::Loader automates the definition of a
DBIx::Class::Schema by scanning database table definitions and
setting up the columns, primary keys, and relationships.

DBIx::Class::Schema::Loader currently supports only the DBI storage type.
It has explicit support for DBD::Pg, DBD::mysql, DBD::DB2, and
DBD::SQLite.  Other DBI drivers may function to a greater or lesser
degree with this loader, depending on how much of the DBI spec they
implement, and how standard their implementation is.  Patches to make
other DBDs work correctly welcome.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DBIx/Class/Schema/*.pm
%{perl_vendorlib}/DBIx/Class/Schema/Loader
%{_mandir}/man3/*