%define name cpp2latex
%define version 2.3
%define release 2

Summary:	Converts C/C++ code to a LaTeX file
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/C++
Url:		https://www.arnoldarts.de/drupal/?q=Cpp2LaTeX
Source0:	http://www.arnoldarts.de/drupal/files/downloads/cpp2latex/%{name}-%{version}.tar.bz2
BuildRequires:	flex
Requires:	tetex-latex
Patch1:		cpp2latex-2.3-gcc43.patch
Patch0:		cpp2latex-2.3.patch
Patch2:		cpp2latex-2.3-tests.patch

%description
cpp2latex takes as input a C or C++ source file and outputs a LaTeX
file that is a beautified listing (optionally the output can contain
the 'documentstyle' header and so on).

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
./configure --prefix=%{_prefix}
%make CFLAGS="-DC_PLUSPLUS $RPM_OPT_FLAGS"

%install
%makeinstall_std

%files
%doc README ChangeLog
%{_bindir}/cpp2latex
