Summary:        Physical simulator which allows to construct objects using different materials
Name:           powder
Version:        70.1
Release:        2
License:        GPLv2
Group:          Games/Other
Source:         %{name}-%{version}.tar.bz2
Patch0:		lua5.1.patch
Patch1:		sse.patch
URL:            https://powder.hardwired.org.uk/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  SDL-devel
BuildRequires:  fftw-devel
BuildRequires:  bzip2-devel
BuildRequires:  lua5.1-devel

%description
Physical simulator which allows constructing your own objects
such as volcano or calculator using different materials

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make

%install
install -D -m 0755 build/powder %{buildroot}%{_bindir}/powder
install -D -m 0644 src/Resources/Icon-32.png %{buildroot}%{_datadir}/pixmaps/powder.png
#install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/powder.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/powder
#%{_datadir}/applications/powder.desktop
%{_datadir}/pixmaps/powder.png



%changelog
* Tue Dec 27 2011 Denis Silakov <dsilakov@mandriva.org> 70.1-1
+ Revision: 745551
- Add sse patch
- Fix fftw build dependency
- Import powder sources
- Import powder
- Created package structure for powder.

