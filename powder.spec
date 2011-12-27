Summary:        Physical simulator which allows to construct objects using different materials
Name:           powder
Version:        70.1
Release:        1
License:        GPLv2
Group:          Games/Other
Source:         %{name}-%{version}.tar.bz2
Patch0:		lua5.1.patch
URL:            http://powder.hardwired.org.uk/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  SDL-devel
BuildRequires:  fftw3-devel = 3.2.2-4
BuildRequires:  lua5.1-devel

%description
Physical simulator which allows constructing your own objects
such as volcano or calculator using different materials

%prep
%setup -q
%patch0 -p1

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

