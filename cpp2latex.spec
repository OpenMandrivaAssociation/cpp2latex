%define name cpp2latex
%define version 2.3
%define release %mkrel 4

Summary:	Converts C/C++ code to a LaTeX file
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/C++
Url:		http://www.arnoldarts.de/drupal/?q=Cpp2LaTeX
Source:		http://www.arnoldarts.de/drupal/files/downloads/cpp2latex/%{name}-%{version}.tar.bz2
BuildRequires:	flex
Buildroot:	%{_tmppath}/%{name}-buildroot
Requires:	tetex-latex

%description
cpp2latex takes as input a C or C++ source file and outputs a LaTeX
file that is a beautified listing (optionally the output can contain
the 'documentstyle' header and so on).

%prep
%setup

%build
%configure
%make CFLAGS="-DC_PLUSPLUS $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README ChangeLog
%{_bindir}/cpp2latex

